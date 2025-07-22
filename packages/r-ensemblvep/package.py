# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsemblvep(RPackage):
	"""R Interface to Ensembl Variant Effect Predictor

	Query the Ensembl Variant Effect Predictor via the perl API.
	"""
	
	bioc = "ensemblVEP"

	version("1.44.0", commit="58d05c04229d388316c20835de134fe12820ad03")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
