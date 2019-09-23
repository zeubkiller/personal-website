from app.application import ServerApplication

#Server creation
serverApp = ServerApplication.initialize_server()

#Dependency creation
ServerApplication.initialize_dependencies(serverApp)

#Blueprint registration
ServerApplication.blueprint_registration(serverApp)
