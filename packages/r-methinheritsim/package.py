# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethinheritsim(RPackage):
	"""Simulating Whole-Genome Inherited Bisulphite Sequencing Data

	Simulate a multigeneration methylation case versus control experiment with inheritance relation using a real control dataset.
	"""
	
	homepage = "https://github.com/belleau/methInheritSim"
	bioc = "methInheritSim" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/methInheritSim_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/methInheritSim/methInheritSim_1.24.0.tar.gz"]

	version("1.24.0", sha256="1c71c13b023b3806790ed1982761488db186c9d49c973f3a27b401d64ae04f87")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-methylkit", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
