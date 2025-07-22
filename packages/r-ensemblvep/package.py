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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ensemblVEP_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ensemblVEP/ensemblVEP_1.44.0.tar.gz"]

	version("1.44.0", sha256="c654f9b3030d23b68528471f51e726931c4478e43907616ad0302ad51f7af4cd")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
