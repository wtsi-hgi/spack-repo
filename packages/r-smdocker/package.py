# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmdocker(RPackage):
	"""Build 'Docker Images' in 'Amazon SageMaker Studio' using 'Amazon
Web Service CodeBuild'

	Allows users to easily build custom 'docker images' <https://docs.docker.com/> from
    'Amazon Web Service Sagemaker' <https://aws.amazon.com/sagemaker/> using
    'Amazon Web Service CodeBuild' <https://aws.amazon.com/codebuild/>.
	"""
	
	homepage = "https://github.com/DyfanJones/sm-docker"
	cran = "smdocker" 

	version("0.1.4", md5="7e8461ee70b2f78d397e7d2d364fc7b0")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-paws-compute", type=("build", "run"))
	depends_on("r-paws-developer-tools", type=("build", "run"))
	depends_on("r-paws-machine-learning", type=("build", "run"))
	depends_on("r-paws-management", type=("build", "run"))
	depends_on("r-paws-storage", type=("build", "run"))
	depends_on("r-paws-security-identity", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
