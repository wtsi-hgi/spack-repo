# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrafzahl(RPackage):
	"""Supervised Machine Learning for Textual Data Using Transformers
and 'Quanteda'

	Duct tape the 'quanteda' ecosystem (Benoit et al., 2018) <doi:10.21105/joss.00774> to modern Transformer-based text classification models (Wolf et al., 2020) <doi:10.18653/v1/2020.emnlp-demos.6>, in order to facilitate supervised machine learning for textual data. This package mimics the behaviors of 'quanteda.textmodels' and provides a function to setup the 'Python' environment to use the pretrained models from 'Hugging Face' <https://huggingface.co/>. More information: <doi:10.5117/CCR2023.1.003.CHAN>.
	"""
	
	homepage = "https://gesistsa.github.io/grafzahl/"
	cran = "grafzahl" 

	version("0.0.8", md5="644abcb67c793271446fef255530816a")
	version("0.0.11", md5="0ecf78f2c0f7231591ca40c1c60f5de2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lime", type=("build", "run"))
	depends_on("r-quanteda", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
