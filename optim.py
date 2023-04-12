from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from scipy.optimize import differential_evolution

# On créé un espace aléatoire de régression (pour l'exemple)
# 2 variables d'entrées x1 et x2 et une cible y
X, y = make_regression(n_samples=1000000, n_features=2, noise=3, random_state=42)

print('Forme tenseur des variables',X.shape)
print('Forme tenseur de la cible',y.shape)

print('\n5 premières lignes de X:\n')
print(X[:5])

print('\n5 premières lignes de y:\n')
print(y[:5])

# On sépare les données en 1 jeu d'entrainement et 1 jeu de test (80%-20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# On définit une fonction d'erreur qui calcul l'écart entre la prédiction et 

def error_function(p):
    # p est la liste des paramètres de l'équation
    # équation de la forme p0*x1 + p1*x2 + p3*x1² + p4*x2² + p5*X1*x2
    # X[:,i] permet d'accéder à la colonne i de X (y_pred est un vecteur donc)
    
    y_pred = p[0]*X_train[:,0] + p[1]*X_train[:,1] + p[2]*X_train[:,0]**2 + \
        p[3]*X_train[:,1]**2 + p[4]*X_train[:,0]*X_train[:,1]
    
    # La fonction retourne l'erreur moyenne quadratique entre les prédiction et les valeures vraies
    return mean_squared_error(y_train, y_pred)

# On borne l'intervalle de recherche des paramètres (empirique)
bounds = [(-100, 100),(-100, 100),(-100, 100),(-100, 100),(-100, 100)]

# Calcul des paramètres optimaux (peu prendre du temps)
print('\n>>> Calcul optimisation...\n')
result = differential_evolution(error_function, bounds)

# résultats de l'optimisation (meilleurs paramètres pi)
p = result.x
print('>>> Meilleurs paramètres:',p)

# Calcul de y sur le jeu de test avec ces paramètres
y_pred_test = p[0]*X_test[:,0] + p[1]*X_test[:,1] + p[2]*X_test[:,0]**2 + \
        p[3]*X_test[:,1]**2 + p[4]*X_test[:,0]*X_test[:,1]

print('\n5 premières lignes de y_test:\n')
print(y_test[:5])

print('\n5 premières lignes de y_pred_test:\n')
print(y_pred_test[:5])

# Calcul R² sur le jeu de test
print('\nR2 sur le jeu de test:',r2_score(y_test, y_pred_test))
