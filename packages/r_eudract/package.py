# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REudract(RPackage):
	"""Creates Safety Results Summary in XML to Upload to EudraCT, or
ClinicalTrials.gov

	The remit of the European Clinical Trials Data Base (EudraCT <https://eudract.ema.europa.eu/> ), or ClinicalTrials.gov <https://clinicaltrials.gov/>, is to provide open access to summaries of all registered clinical trial results; thus aiming to prevent non-reporting of negative results and provide open-access to results to inform future research. The amount of information required and the format of the results, however, imposes a large extra workload at the end of studies on clinical trial units. In particular, the adverse-event-reporting component requires entering: each unique combination of treatment group and safety event; for every such event above, a further 4 pieces of information (body system, number of occurrences, number of subjects, number exposed) for non-serious events, plus an extra three pieces of data for serious adverse events (numbers of causally related events, deaths, causally related deaths). This package prepares the required statistics needed by EudraCT and formats them into the precise requirements to directly upload an XML file into the web portal, with no further data entry by hand.
	"""
	
	homepage = "https://eudract-tool.medschl.cam.ac.uk/"
	cran = "eudract" 

	version("1.0.0", md5="d4775e0724d428dd3d7a2424ae075f32")
	version("0.10.2", md5="c0b1a975db1308adf715160d37c9f93c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xslt", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
