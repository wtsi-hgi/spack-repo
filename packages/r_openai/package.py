# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenai(RPackage):
	"""R Wrapper for OpenAI API

	An R wrapper of OpenAI API endpoints (see
    <https://platform.openai.com/docs/introduction> for details). This package
    covers Models, Completions, Chat, Edits, Images, Embeddings, Audio, Files,
    Fine-tunes, Moderations, and legacy Engines endpoints.
	"""
	
	homepage = "https://github.com/irudnyts/openai"
	cran = "openai" 

	version("0.4.1", md5="6187b6afa7b157fb4531c9b78ec2c1dd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-httr@1.4.3:", type=("build", "run"))
	depends_on("r-jsonlite@1.8:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.1:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
