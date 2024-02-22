# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoisyr(RPackage):
	"""Noise Quantification in High Throughput Sequencing Output

	Quantifies and removes technical noise from high-throughput 
        sequencing data. Two approaches are used, one based on the count
        matrix, and one using the alignment BAM files directly.
        Contains several options for every step of the process, as well
        as tools to quality check and assess the stability of output.
	"""
	
	homepage = "https://github.com/Core-Bioinformatics/noisyR"
	cran = "noisyr" 

	version("1.0.0", md5="970c060f9754927acdbb2af41ac01dea")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-philentropy", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
