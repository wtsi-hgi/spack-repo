# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhipdata(RPackage):
	"""Container for PhIP-Seq Experiments

	PhIPData defines an S4 class for phage-immunoprecipitation sequencing (PhIP-seq) experiments. Buliding upon the RangedSummarizedExperiment class, PhIPData enables users to coordinate metadata with experimental data in analyses. Additionally, PhIPData provides specialized methods to subset and identify beads-only samples, subset objects using virus aliases, and use existing peptide libraries to populate object parameters.
	"""
	
	bioc = "PhIPData" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PhIPData_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PhIPData/PhIPData_1.10.0.tar.gz"]

	version("1.10.0", sha256="8fc30e49ba8dcf8f474ac6f68019da846c971f0be9a1a31692ef6a65f6c2a892")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.3.81:", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
