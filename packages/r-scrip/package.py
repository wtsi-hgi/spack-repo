# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrip(RPackage):
	"""An Accurate Simulator for Single-Cell RNA Sequencing Data

	We provide a comprehensive scheme that is capable of simulating Single Cell RNA Sequencing data for various parameters of Biological Coefficient of Variation,
    busting kinetics, differential expression (DE), cell or sample groups, cell trajectory, batch effect and other experimental designs.
    'SCRIP' proposed and compared two frameworks with Gamma-Poisson and Beta-Gamma-Poisson models for simulating Single Cell RNA Sequencing data.
	Other reference is available in Zappia et al. (2017) <https://genomebiology.biomedcentral.com/articles/10.1186/s13059-017-1305-0>.
	"""
	
	homepage = "https://github.com/thecailab/SCRIP"
	cran = "SCRIP" 

	version("1.0.0", md5="8749f941f0a1c8be84a7747574a0b9f0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-splatter@1.16.1:", type=("build", "run"))
	depends_on("r-s4vectors@0.30:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.22:", type=("build", "run"))
	depends_on("r-singlecellexperiment@1.14.1:", type=("build", "run"))
	depends_on("r-edger@3.34:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
