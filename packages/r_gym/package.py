# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGym(RPackage):
	"""Provides Access to the OpenAI Gym API

	OpenAI Gym is a open-source Python toolkit for developing and comparing
    reinforcement learning algorithms. This is a wrapper for the OpenAI Gym API,
    and enables access to an ever-growing variety of environments.
    For more details on OpenAI Gym, please see here: <https://github.com/openai/gym>.
    For more details on the OpenAI Gym API specification, please see here:
    <https://github.com/openai/gym-http-api>.
	"""
	
	homepage = "https://github.com/paulhendricks/gym-R"
	cran = "gym" 

	version("0.1.0", md5="5f21078273f0101e49a9fcecf636d86f")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
