# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKonfound(RPackage):
	"""Quantify the Robustness of Causal Inferences

	Statistical methods that quantify the conditions necessary to
    alter inferences, also known as sensitivity analysis, are becoming
    increasingly important to a variety of quantitative sciences. A series
    of recent works, including Frank (2000)
    <doi:10.1177/0049124100029002001> and Frank et al.  (2013)
    <doi:10.3102/0162373713493129> extend previous sensitivity analyses by
    considering the characteristics of omitted variables or unobserved
    cases that would change an inference if such variables or cases were
    observed. These analyses generate statements such as "an omitted
    variable would have to be correlated at xx with the predictor of
    interest (e.g., treatment) and outcome to invalidate an inference of a
    treatment effect". Or "one would have to replace pp percent of the
    observed data with null hypothesis cases to invalidate the inference".
    We implement these recent developments of sensitivity analysis and
    provide modules to calculate these two robustness indices and generate
    such statements in R. In particular, the functions konfound(),
    pkonfound() and mkonfound() allow users to calculate the robustness of
    inferences for a user's own model, a single published study and
    multiple studies respectively.
	"""
	
	homepage = "https://github.com/konfound-project/konfound"
	cran = "konfound" 

	version("0.5.0", md5="55745d04c7a38aa0728d98735970bc60")
	version("0.4.0", md5="e4d3c73fc9b7f827310a55de8e4407ad")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-broom-mixed", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lme4@1.1.35.1:", type=("build", "run"))
	depends_on("r-margins", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-pbkrtest", type=("build", "run"))
