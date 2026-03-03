# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixchar(RPackage):
	"""Mixture Model for the Deconvolution of Thermal Decay Curves

	Deconvolution of thermal decay curves allows you to quantify proportions 
    of biomass components in plant litter. Thermal decay curves derived from 
    thermogravimetric analysis (TGA) are imported, modified, and then modelled in a 
    three- or four- part  mixture model using the Fraser-Suzuki function. The output 
    is estimates for weights of pseudo-components corresponding to hemicellulose, 
    cellulose, and lignin. For more information see: Müller-Hagedorn, M. and Bockhorn, 
    H. (2007) <doi:10.1016/j.jaap.2006.12.008>, Órfão, J. J. M. and Figueiredo, J. L. 
    (2001) <doi:10.1016/S0040-6031(01)00634-7>, and Yang, H. and Yan, R. and 
    Chen, H. and Zheng, C. and Lee, D. H. and Liang, D. T. (2006) <doi:10.1021/ef0580117>.
	"""
	
	homepage = "http://github.com/smwindecker/mixchar"
	cran = "mixchar" 

	version("0.1.0", md5="c311ef7ec9402142d837a67bf06382f4")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
