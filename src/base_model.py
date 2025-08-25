from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input,Embedding,Dot,Flatten,Dense,Activation,BatchNormalization
from utils.common_function import get_logger,read_yaml_file
from src.custom_exception import CustomExeption

logger = get_logger(__name__)

class BaseModel:
    def __init__(self,config_path):
        try:
            self.config = read_yaml_file(config_path)
            logger.info("Loded configuration from config.yaml.........")
        except Exception as e:
            raise CustomExeption("Error loading configuration",e)
        
    def RecommenderNet(self,n_users,n_anime):
        try:
            embedding_size = self.config["model"]["embedding_size"]

            user = Input(name="user",shape=[1])

            user_embedding = Embedding(name="user_embedding",input_dim=n_users,output_dim=embedding_size)(user)

            anime = Input(name="anime",shape=[1])

            anime_embedding = Embedding(name="anime_embedding",input_dim=n_anime,output_dim=embedding_size)(anime)

            x = Dot(name="dot_product" , normalize=True , axes=2)([user_embedding,anime_embedding])

            x = Flatten()(x)

            x = Dense(1,kernel_initializer='he_normal')(x)
            x = BatchNormalization()(x)
            x = Activation("sigmoid")(x)

            model = Model(inputs=[user,anime], outputs=x)
            model.compile(
                loss = self.config["model"]["loss"],
                optimizer = self.config["model"]["optimizer"],
                metrics = self.config["model"]["metrics"]
            )
            logger.info("Model build successfully")
            return model
        
        except Exception as e:
            logger.error("Error in the model.........")
            raise CustomExeption("Failed to create the model..........",e)
        