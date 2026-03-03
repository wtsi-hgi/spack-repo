# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrmetrics(RPackage):
	"""Cell Ranger Output Filtering and Metrics Visualization

	Sample and cell filtering as well as visualisation of output metrics from 'Cell Ranger' by Grace X.Y. Zheng et al. (2017) <doi:10.1038/ncomms14049>. 'CRMetrics' allows for easy plotting of output metrics across multiple samples as well as comparative plots including statistical assessments of these. 'CRMetrics' allows for easy removal of ambient RNA using 'SoupX' by Matthew D Young and Sam Behjati (2020) <doi:10.1093/gigascience/giaa151> or 'CellBender' by Stephen J Fleming et al. (2022) <doi:10.1101/791699>. Furthermore, it is possible to preprocess data using 'Pagoda2' by Nikolas Barkas et al. (2021) <https://github.com/kharchenkolab/pagoda2> or 'Seurat' by Yuhan Hao et al. (2021) <doi:10.1016/j.cell.2021.04.048> followed by embedding of cells using 'Conos' by Nikolas Barkas et al. (2019) <doi:10.1038/s41592-019-0466-z>. Finally, doublets can be detected using 'scrublet' by Samuel L. Wolock et al. (2019) <doi:10.1016/j.cels.2018.11.005> or 'DoubletDetection' by Gayoso et al. (2020) <doi:10.5281/zenodo.2678041>. In the end, cells are filtered based on user input for use in downstream applications.
	"""
	
	homepage = "https://github.com/khodosevichlab/CRMetrics"
	cran = "CRMetrics" 

	version("0.3.0", md5="cf23b2d4c5aeac77cdefa01ab94a1ca7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggbeeswarm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpmisc", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sccore", type=("build", "run"))
	depends_on("r-sparsematrixstats", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
