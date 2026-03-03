# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmri(RPackage):
	"""Analysis of fMRI Experiments

	Contains R-functions to perform an fMRI analysis as described in
             Polzehl and Tabelow (2019) <DOI:10.1007/978-3-030-29184-6>,
             Tabelow et al. (2006) <DOI:10.1016/j.neuroimage.2006.06.029>,
             Polzehl et al. (2010) <DOI:10.1016/j.neuroimage.2010.04.241>,
             Tabelow and Polzehl (2011) <DOI:10.18637/jss.v044.i11>.
	"""
	
	homepage = "https://www.wias-berlin.de/software/imaging/"
	cran = "fmri" 

	version("1.9.12", md5="b026c50750027696194f429e0becc0f8")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-aws@2.5.1:", type=("build", "run"))
	depends_on("r-oro-nifti", type=("build", "run"))
