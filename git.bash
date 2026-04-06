# Iniciar el repositorio de git
git init

# Crear rama
git checkout -b feature/tasks

# Add y commit
git add .
git commit -m "feat: implementar endpoints de tareas e infraestructura base"

# Agregar remote
git remote add origin <url_del_repositorio>

# Push de la rama
git push -u origin feature/tasks

#-------------------------------------------

# Levantar los contenedores
docker compose up -d

# Bajar contenedores
docker compose down