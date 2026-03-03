# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrainer(RPackage):
	"""Predictive (Classification and Regression) Models Homologator

	Methods to unify the different ways of creating predictive models and their different predictive formats for classification and regression. It includes 
       methods such as K-Nearest Neighbors Schliep, K. P. (2004) <doi:10.5282/ubm/epub.1769>, Decision Trees Leo Breiman, Jerome H. Friedman, Richard A. Olshen, Charles J. Stone (2017) <doi:10.1201/9781315139470>, 
       ADA Boosting Esteban Alfaro, Matias Gamez, Noelia García (2013) <doi:10.18637/jss.v054.i02>, Extreme Gradient Boosting Chen & Guestrin (2016) <doi:10.1145/2939672.2939785>, 
       Random Forest Breiman (2001) <doi:10.1023/A:1010933404324>, Neural Networks Venables, W. N., & Ripley, B. D. (2002) <ISBN:0-387-95457-0>,
       Support Vector Machines Bennett, K. P. & Campbell, C. (2000) <doi:10.1145/380995.380999>, Bayesian Methods Gelman, A., Carlin, J. B., Stern, H. S., & Rubin, D. B. (1995) <doi:10.1201/9780429258411>, 
       Linear Discriminant Analysis Venables, W. N., & Ripley, B. D. (2002) <ISBN:0-387-95457-0>, Quadratic Discriminant Analysis Venables, W. N., & Ripley, B. D. (2002) <ISBN:0-387-95457-0>, 
       Logistic Regression Dobson, A. J., & Barnett, A. G. (2018) <doi:10.1201/9781315182780> and Penalized Logistic Regression Friedman, J. H., Hastie, T., & Tibshirani, R. (2010) <doi:10.18637/jss.v033.i01>.
	"""
	
	homepage = "https://promidat.website/"
	cran = "traineR" 

	version("2.2.0", md5="a79df3a64f508d7940cbd33f51090393")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-neuralnet@1.44.2:", type=("build", "run"))
	depends_on("r-rpart@4.1.13:", type=("build", "run"))
	depends_on("r-xgboost@0.81.0.1:", type=("build", "run"))
	depends_on("r-randomforest@4.6.14:", type=("build", "run"))
	depends_on("r-e1071@1.7.0.1:", type=("build", "run"))
	depends_on("r-kknn@1.3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
	depends_on("r-mass@7.3.53:", type=("build", "run"))
	depends_on("r-ada@2.0.5:", type=("build", "run"))
	depends_on("r-nnet@7.3.12:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-adabag", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
