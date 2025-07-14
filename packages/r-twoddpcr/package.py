# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwoddpcr(RPackage):
	"""Classify 2-d Droplet Digital PCR (ddPCR) data and quantify the number of starting molecules

	The twoddpcr package takes Droplet Digital PCR (ddPCR) droplet amplitude data from Bio-Rad's QuantaSoft and can classify the droplets. A summary of the positive/negative droplet counts can be generated, which can then be used to estimate the number of molecules using the Poisson distribution. This is the first open source package that facilitates the automatic classification of general two channel ddPCR data. Previous work includes 'definetherain' (Jones et al., 2014) and 'ddpcRquant' (Trypsteen et al., 2015) which both handle one channel ddPCR experiments only. The 'ddpcr' package available on CRAN (Attali et al., 2016) supports automatic gating of a specific class of two channel ddPCR experiments only.
	"""
	
	homepage = "http://github.com/CRUKMI-ComputationalBiology/twoddpcr/"
	bioc = "twoddpcr"

	version("1.32.0", commit="33954ebc43cfbabfe5e1df8bab10afea0d7eff2c")
	version("1.26.0", commit="900be64dd14094d8c927f4370f6f711b1f168599")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
