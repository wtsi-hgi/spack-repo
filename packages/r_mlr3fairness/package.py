# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3fairness(RPackage):
	"""Fairness Auditing and Debiasing for 'mlr3'

	
    Integrates fairness auditing and bias mitigation methods for the 'mlr3' ecosystem.
    This includes fairness metrics, reporting tools, visualizations and bias mitigation techniques such as
    "Reweighing" described in 'Kamiran, Calders' (2012) <doi:10.1007/s10115-011-0463-8>  and
    "Equalized Odds" described in 'Hardt et al.' (2016) <https://papers.nips.cc/paper/2016/file/9d2682367c3935defcb1f9e247a97c0d-Paper.pdf>.
    Integration with 'mlr3' allows for auditing of ML models as well as convenient joint tuning of
    machine learning algorithms and debiasing methods.
	"""
	
	homepage = "https://mlr3fairness.mlr-org.com"
	cran = "mlr3fairness" 

	version("0.3.2", md5="9be180af7d2b07033927bd77e2549a16")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-r6@2.4.1:", type=("build", "run"))
	depends_on("r-data-table@1.13.6:", type=("build", "run"))
	depends_on("r-paradox", type=("build", "run"))
	depends_on("r-mlr3@0.13:", type=("build", "run"))
	depends_on("r-mlr3measures", type=("build", "run"))
	depends_on("r-mlr3misc", type=("build", "run"))
	depends_on("r-mlr3pipelines", type=("build", "run"))
	depends_on("r-mlr3learners", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
