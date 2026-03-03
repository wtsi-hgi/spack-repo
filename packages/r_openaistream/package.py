# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenaistream(RPackage):
	"""Streaming Capabilities for 'OpenAI API' Interactions

	Based on the 'httr2' framework, the 'OpenAI' interface supports streaming calls and model training. 
             For more details on the API methods implemented, see the 'OpenAI' platform documentation at <https://platform.openai.com/docs/api-reference>.
	"""
	
	homepage = "https://github.com/libingfei/openaistream"
	cran = "openaistream" 

	version("0.2.0", md5="70d7fb45216b34614aa57c365873a881")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.8.7:", type=("build", "run"))
	depends_on("r-httr2@0.2.3:", type=("build", "run"))
	depends_on("r-r6@2.5.1:", type=("build", "run"))
	depends_on("r-iterators@1.0.14:", type=("build", "run"))
	depends_on("r-curl@5.1:", type=("build", "run"))
