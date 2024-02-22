# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFundata(RPackage):
	"""An S4 Class for Functional Data

	S4 classes for univariate and multivariate functional data with
    utility functions. See <doi:10.18637/jss.v093.i05> for a detailed description 
    of the package functionalities and its interplay with the MFPCA package for 
    multivariate functional principal component analysis 
    <https://CRAN.R-project.org/package=MFPCA>. 
	"""
	
	homepage = "https://github.com/ClaraHapp/funData"
	cran = "funData" 

	version("1.3-9", md5="c09e1a54edadc53fbaaa1ec2d072b632")

	depends_on("r-abind", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
