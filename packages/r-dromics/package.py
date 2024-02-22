# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDromics(RPackage):
	"""Dose Response for Omics

	Several functions are provided for dose-response (or concentration-response) characterization from omics data. 'DRomics' is especially dedicated to omics data obtained using a typical dose-response design, favoring a great number of tested doses (or concentrations) rather than a great number of replicates (no need of replicates). 'DRomics' provides functions 1) to check, normalize and or transform data, 2) to select monotonic or biphasic significantly responding items (e.g. probes, metabolites), 3) to choose the best-fit model among a predefined family of monotonic and biphasic models to describe each selected item, 4) to derive a benchmark dose or concentration and a typology of response from each fitted curve. In the available version data are supposed to be single-channel microarray data in log2, RNAseq data in raw counts, or already pretreated continuous omics data (such as metabolomic data) in log scale. In order to link responses across biological levels based on a common method, 'DRomics' also handles apical data as long as they are continuous and follow a normal distribution for each dose or concentration, with a common standard error. For further details see Delignette-Muller et al (2023) <DOI:10.24072/pcjournal.325> and Larras et al (2018) <DOI:10.1021/acs.est.8b04752>.
	"""
	
	homepage = "https://lbbe.univ-lyon1.fr/fr/dromics"
	cran = "DRomics" 

	version("2.5-2", md5="2438a06669dbfc80e7188e769e903fd6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggfortify", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
