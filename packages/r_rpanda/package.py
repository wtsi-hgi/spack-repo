# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpanda(RPackage):
	"""Phylogenetic ANalyses of DiversificAtion

	Implements macroevolutionary analyses on phylogenetic trees. See
    Morlon et al. (2010) <DOI:10.1371/journal.pbio.1000493>, Morlon et al. (2011)
    <DOI:10.1073/pnas.1102543108>, Condamine et al. (2013) <DOI:10.1111/ele.12062>,
    Morlon et al. (2014) <DOI:10.1111/ele.12251>, Manceau et al. (2015) <DOI:10.1111/ele.12415>,
    Lewitus & Morlon (2016) <DOI:10.1093/sysbio/syv116>, Drury et al. (2016) <DOI:10.1093/sysbio/syw020>,
    Manceau et al. (2016) <DOI:10.1093/sysbio/syw115>, Morlon et al. (2016) <DOI:10.1111/2041-210X.12526>, Clavel & Morlon (2017) <DOI:10.1073/pnas.1606868114>,
    Drury et al. (2017) <DOI:10.1093/sysbio/syx079>, Lewitus & Morlon (2017) <DOI:10.1093/sysbio/syx095>,
    Drury et al. (2018) <DOI:10.1371/journal.pbio.2003563>, Clavel et al. (2019) <DOI:10.1093/sysbio/syy045>, Maliet et al. (2019) <DOI:10.1038/s41559-019-0908-0>,
    Billaud et al. (2019) <DOI:10.1093/sysbio/syz057>, Lewitus et al. (2019) <DOI:10.1093/sysbio/syz061>,
    Aristide & Morlon (2019) <DOI:10.1111/ele.13385>, Maliet et al. (2020) <DOI:10.1111/ele.13592>, Drury et al. (2021) <DOI:10.1371/journal.pbio.3001270>,
    Perez-Lamarque & Morlon (2022) <DOI:10.1111/mec.16478>, Perez-Lamarque et al. (2022) <DOI:10.1101/2021.08.30.458192>, Mazet et al. (2023) <DOI:10.1111/2041-210X.14195>, Drury et al. (2024) <DOI:10.1016/j.cub.2023.12.055>.
	"""
	
	homepage = "https://github.com/hmorlon/PANDA"
	cran = "RPANDA" 

	version("2.3", md5="b2c61fad588e77d2fbb82523a8aaa4a5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-picante", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-bipartite", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-geiger", type=("build", "run"))
	depends_on("r-glassofast", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mvmorph@1.1.6:", type=("build", "run"))
	depends_on("r-gunifrac", type=("build", "run"))
	depends_on("r-parallellogger", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-pspline", type=("build", "run"))
	depends_on("r-pvclust", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-tess", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
