# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsoplotr(RPackage):
	"""Statistical Toolbox for Radiometric Geochronology

	Plots U-Pb data on Wetherill and Tera-Wasserburg concordia diagrams. Calculates concordia and discordia ages. Performs linear regression of measurements with correlated errors using 'York', 'Titterington', 'Ludwig' and Omnivariant Generalised Least-Squares ('OGLS') approaches. Generates Kernel Density Estimates (KDEs) and Cumulative Age Distributions (CADs). Produces Multidimensional Scaling (MDS) configurations and Shepard plots of multi-sample detrital datasets using the Kolmogorov-Smirnov distance as a dissimilarity measure. Calculates 40Ar/39Ar ages, isochrons, and age spectra. Computes weighted means accounting for overdispersion. Calculates U-Th-He (single grain and central) ages, logratio plots and ternary diagrams. Processes fission track data using the external detector method and LA-ICP-MS, calculates central ages and plots fission track and other data on radial (a.k.a. 'Galbraith') plots. Constructs total Pb-U, Pb-Pb, Th-Pb, K-Ca, Re-Os, Sm-Nd, Lu-Hf, Rb-Sr and 230Th-U isochrons as well as 230Th-U evolution plots.
	"""
	
	homepage = "https://www.ucl.ac.uk/~ucfbpve/isoplotr/"
	cran = "IsoplotR" 

	version("6.1", md5="336bd1a5eca3927df34d444374a0db8c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
