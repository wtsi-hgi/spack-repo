# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNegligible(RPackage):
	"""A Collection of Functions for Negligible Effect/Equivalence
Testing

	Researchers often want to evaluate whether there is a negligible
    relationship among variables. The 'negligible' package provides functions that 
    are useful for conducting negligible effect testing (also called
    equivalence testing). For example, there are functions for evaluating the 
    equivalence of means or the presence of a negligible association 
    (correlation or  regression). Beribisky, N., Mara, C., & Cribbie, R. A. (2020) <doi:10.20982/tqmp.16.4.p424>.
    Beribisky, N., Davidson, H., Cribbie, R. A. (2019) <doi:10.7717/peerj.6853>.
    Shiskina, T., Farmus, L., & Cribbie, R. A. (2018) <doi:10.20982/tqmp.14.3.p167>.
    Mara, C. & Cribbie, R. A. (2017) <doi:10.1080/00220973.2017.1301356>.
    Counsell, A. & Cribbie, R. A. (2015) <doi:10.1111/bmsp.12045>.
    van Wieringen, K. & Cribbie, R. A. (2014) <doi:10.1111/bmsp.12015>.
    Goertzen, J. R. & Cribbie, R. A. (2010) <doi:10.1348/000711009x475853>.
    Cribbie, R. A., Gruman, J. & Arpin-Cribbie, C. (2004) <doi:10.1002/jclp.10217>.
	"""
	
	cran = "negligible" 

	version("0.1.6", md5="e880197e07850ff2b1ab8e2b75d5f01f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-wrs2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nptest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fungible", type=("build", "run"))
	depends_on("r-rockchalk", type=("build", "run"))
	depends_on("r-mbess", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
