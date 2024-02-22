# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPompom(RPackage):
	"""Person-Oriented Method and Perturbation on the Model

	An implementation of a hybrid method of person-oriented method and perturbation on the model. Pompom is the initials of the two methods. The hybrid method will provide a multivariate intraindividual variability metric (iRAM). The person-oriented method used in this package refers to uSEM (unified structural equation modeling, see Kim et al., 2007, Gates et al., 2010 and Gates et al., 2012 for details). Perturbation on the model was conducted according to impulse response analysis introduced in Lutkepohl (2007). 
    Kim, J., Zhu, W., Chang, L., Bentler, P. M., & Ernst, T. (2007) <doi:10.1002/hbm.20259>. 
    Gates, K. M., Molenaar, P. C. M., Hillary, F. G., Ram, N., & Rovine, M. J. (2010) <doi:10.1016/j.neuroimage.2009.12.117>. 
    Gates, K. M., & Molenaar, P. C. M. (2012) <doi:10.1016/j.neuroimage.2012.06.026>. 
    Lutkepohl, H. (2007, ISBN:3540262393).
	"""
	
	cran = "pompom" 

	version("0.2.1", md5="16ac4a99bbf7220f69173c86567e82a2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lavaan@0.5.23.1097:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.2:", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
