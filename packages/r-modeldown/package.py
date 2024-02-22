# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModeldown(RPackage):
	"""Make Static HTML Website for Predictive Models

	Website generator with HTML summaries for predictive models.
    This package uses 'DALEX' explainers to describe global model behavior. 
    We can see how well models behave (tabs: Model Performance, Auditor),
    how much each variable contributes to predictions (tabs: Variable Response) 
    and which variables are the most important for a given model (tabs: Variable Importance).
    We can also compare Concept Drift for pairs of models (tabs: Drifter).
    Additionally, data available on the website can be easily recreated in current R session.
    Work on this package was financially supported by the NCN Opus grant 2017/27/B/ST6/01307 
    at Warsaw University of Technology, Faculty of Mathematics and Information Science.
	"""
	
	homepage = "https://github.com/ModelOriented/modelDown"
	cran = "modelDown" 

	version("1.1", md5="1c5a0ef55772483244d84a79ffde05b7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dalex@1:", type=("build", "run"))
	depends_on("r-auditor@0.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-whisker@0.3.2:", type=("build", "run"))
	depends_on("r-dt@0.4:", type=("build", "run"))
	depends_on("r-kableextra@0.9:", type=("build", "run"))
	depends_on("r-psych@1.8.4:", type=("build", "run"))
	depends_on("r-archivist@2.1:", type=("build", "run"))
	depends_on("r-svglite@1.2.1:", type=("build", "run"))
	depends_on("r-devtools@2.0.1:", type=("build", "run"))
	depends_on("r-breakdown@0.1.6:", type=("build", "run"))
	depends_on("r-drifter@0.2.1:", type=("build", "run"))
