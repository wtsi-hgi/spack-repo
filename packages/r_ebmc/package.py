# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbmc(RPackage):
	"""Ensemble-Based Methods for Class Imbalance Problem

	Four ensemble-based methods (SMOTEBoost, RUSBoost, UnderBagging, and SMOTEBagging) for class imbalance problem are implemented for binary classification. Such methods adopt ensemble methods and data re-sampling techniques to improve model performance in presence of class imbalance problem. One special feature offers the possibility to choose multiple supervised learning algorithms to build weak learners within ensemble models. References: Nitesh V. Chawla, Aleksandar Lazarevic, Lawrence O. Hall, and Kevin W. Bowyer (2003) <doi:10.1007/978-3-540-39804-2_12>, Chris Seiffert, Taghi M. Khoshgoftaar, Jason Van Hulse, and Amri Napolitano (2010) <doi:10.1109/TSMCA.2009.2029559>, R. Barandela, J. S. Sanchez, R. M. Valdovinos (2003) <doi:10.1007/s10044-003-0192-z>, Shuo Wang and Xin Yao (2009) <doi:10.1109/CIDM.2009.4938667>, Yoav Freund and Robert E. Schapire (1997) <doi:10.1006/jcss.1997.1504>.
	"""
	
	cran = "ebmc" 

	version("1.0.1", md5="c22b0d13c1927d4c36960081b8dfa560")

	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-c50", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-smotefamily", type=("build", "run"))
