# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeuristicsminer(RPackage):
	"""Discovery of Process Models with the Heuristics Miner

	Provides the heuristics miner algorithm for process discovery 
   as proposed by Weijters et al. (2011) <doi:10.1109/CIDM.2011.5949453>. The
   algorithm builds a causal net from an event log created with the 'bupaR' 
   package. Event logs are a set of ordered sequences of events for which 
   'bupaR' provides the S3 class eventlog(). The discovered causal nets 
   can be visualised as 'htmlwidgets' and it is possible to annotate them with
   the occurrence frequency or processing and waiting time of process 
   activities.  
	"""
	
	homepage = "https://github.com/bupaverse/heuristicsmineR"
	cran = "heuristicsmineR" 

	version("0.3.0", md5="17c10edd0355cf4f93a16de54872cef5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bupar", type=("build", "run"))
	depends_on("r-processmapr@0.3.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-diagrammer@1:", type=("build", "run"))
	depends_on("r-petrinetr@0.3:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
