# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatanugget(RPackage):
	"""Create, and Refine Data Nuggets

	Creating, and refining data nuggets. 
    Data nuggets reduce a large dataset into a small collection of nuggets of 
    data, each containing a center (location), weight (importance), and scale 
    (variability) parameter. Data nugget centers are created by choosing 
    observations in the dataset which are as equally spaced apart as possible. 
    Data nugget weights are created by counting the number observations 
    closest to a given data nugget’s center. We then say the data nugget 
    'contains' these observations and the data nugget center is recalculated 
    as the mean of these observations. Data nugget scales are created by 
    calculating the trace of the covariance matrix of the observations 
    contained within a data nugget divided by the dimension of the dataset. 
    Data nuggets are refined by 'splitting' data nuggets which have scales or 
    shapes (defined as the ratio of the two largest eigenvalues of the 
    covariance matrix of the observations contained within the data nugget) 
    Reference paper: [1] Cherasia, K. E., Cabrera, J., Fernholz, L. T., & Fernholz, R. (2022). Data Nuggets in Supervised Learning. emph{In Robust and Multivariate Statistical Methods: Festschrift in Honor of David E. Tyler} (pp. 429-449). Cham: Springer International Publishing. [2] Beavers, T., Cheng, G., Duan, Y., Cabrera, J., Lubomirski, M., Amaratunga, D., Teigler, J. (2023). Data Nuggets: A Method for Reducing Big Data While Preserving Data Structure (Submitted for Publication).
	"""
	
	cran = "datanugget" 

	version("1.2.4", md5="2e6bc6b13153fce9587e38c50bef2191")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dosnow@1.0.16:", type=("build", "run"))
	depends_on("r-foreach@1.5.1:", type=("build", "run"))
	depends_on("r-rfast@2.0.7:", type=("build", "run"))
