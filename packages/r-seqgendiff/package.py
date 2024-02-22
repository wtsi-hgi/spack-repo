# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqgendiff(RPackage):
	"""RNA-Seq Generation/Modification for Simulation

	Generates/modifies RNA-seq data for use in simulations. We provide
    a suite of functions that will add a known amount of signal to a real 
    RNA-seq dataset. The advantage of using this approach over simulating under
    a theoretical distribution is that common/annoying aspects of the data
    are more preserved, giving a more realistic evaluation of your method. 
    The main functions are select_counts(), thin_diff(), thin_lib(), 
    thin_gene(), thin_2group(), thin_all(), and effective_cor(). See
    Gerard (2020) <doi:10.1186/s12859-020-3450-9> for details on the
    implemented methods.
	"""
	
	homepage = "https://github.com/dcgerard/seqgendiff"
	cran = "seqgendiff" 

	version("1.2.3", md5="568d08051362931fc306686d711ee782")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
	depends_on("r-matchingr", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-cate", type=("build", "run"))
