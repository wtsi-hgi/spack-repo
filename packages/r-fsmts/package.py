# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsmts(RPackage):
	"""Feature Selection for Multivariate Time Series

	Implements feature selection routines for multivariate time series (MTS). 
    The list of implemented algorithms includes: 
    own lags (independent MTS components), 
    distance-based (using external structure, e.g. Pfeifer and Deutsch (1980) <doi:10.2307/1268381>),
    cross-correlation (see  Schelter et al. (2006, ISBN:9783527406234)),
    graphical LASSO (see Haworth and Cheng (2014) <https://www.gla.ac.uk/media/Media_401739_smxx.pdf>),
    random forest (see Pavlyuk (2020) "Random Forest Variable Selection for Sparse Vector Autoregressive Models" in Contributions to Statistics, in production),
    least angle regression (see Gelper and Croux (2008) <https://lirias.kuleuven.be/retrieve/16024>), 
    mutual information (see  Schelter et al. (2006, ISBN:9783527406234), Liu et al. (2016) <doi:10.1109/ChiCC.2016.7554480>),
    and partial spectral coherence (see Davis et al.(2016) <doi:10.1080/10618600.2015.1092978>). 
    In addition, the package implements functions for ensemble feature selection (using feature ranking and majority voting).
    The package is implemented within Dmitry Pavlyuk's research project No. 1.1.1.2/VIAA/1/16/112 "Spatiotemporal urban traffic modelling using big data".
	"""
	
	cran = "fsMTS" 

	version("0.1.7", md5="e2800a7aa8e01a551333542fffa1548b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-mpmi", type=("build", "run"))
	depends_on("r-freqdom", type=("build", "run"))
	depends_on("r-randomforestsrc", type=("build", "run"))
