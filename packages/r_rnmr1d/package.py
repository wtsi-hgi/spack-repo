# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnmr1d(RPackage):
	"""Perform the Complete Processing of a Set of Proton Nuclear
Magnetic Resonance Spectra

	Perform the complete processing of a set of proton nuclear magnetic resonance spectra from the free induction decay (raw data) and based on a processing sequence (macro-command file). An additional file specifies all the spectra to be considered by associating their sample code as well as the levels of experimental factors to which they belong. More detail can be found in Jacob et al. (2017) <doi:10.1007/s11306-017-1178-y>.
	"""
	
	homepage = "https://github.com/INRA/Rnmr1D"
	cran = "Rnmr1D" 

	version("1.3.2", md5="fb854f8cbf016d50dbe433863335911e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-base64enc@0.1:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-doparallel@1.0.11:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
	depends_on("r-igraph@1.2.1:", type=("build", "run"))
	depends_on("r-impute@1.54:", type=("build", "run"))
	depends_on("r-massspecwavelet@1.46:", type=("build", "run"))
	depends_on("r-ptw@1.9:", type=("build", "run"))
	depends_on("r-signal@0.7:", type=("build", "run"))
	depends_on("r-xml@3.98:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-plotly@4.8:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-minqa@1.2.4:", type=("build", "run"))
