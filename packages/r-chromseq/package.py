# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChromseq(RPackage):
	"""Split Chromosome 'Fasta' File

	Chromosome files in the 'Fasta' format usually contain large sequences like human genome.
  Sometimes users have to split these chromosomes into different files according to their 
  chromosome number. The 'chromseq' can help to handle this. So the selected chromosome sequence can be
  used for downstream analysis like motif finding. Howard Y. Chang(2019)
  <doi:10.1038/s41587-019-0206-z>.
	"""
	
	homepage = "https://github.com/MSQ-123/chromseq"
	cran = "chromseq" 

	version("0.1.3", md5="6b2283e0c807e7c996f7ea481bf179cd")

	depends_on("r@2.10:", type=("build", "run"))
