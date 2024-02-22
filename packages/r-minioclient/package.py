# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinioclient(RPackage):
	"""Interface to the 'MinIO' Client

	An R interface to the 'MinIO' Client. The 'MinIO' Client ('mc')
  provides a modern alternative to UNIX commands like 'ls', 'cat', 'cp',
  'mirror', 'diff', 'find' etc. It supports 'filesystems'  and Amazon "S3"
  compatible cloud storage service ("AWS" Signature v2 and v4).
  This package provides convenience functions for installing the 'MinIO'
  client and running any operations, as described in the official 
  documentation, <https://min.io/docs/minio/linux/reference/minio-mc.html?ref=docs-redirect>.
  This package provides a flexible and high-performance alternative to 'aws.s3'.
	"""
	
	homepage = "https://github.com/cboettig/minioclient"
	cran = "minioclient" 

	version("0.0.6", md5="60d3711c85531edb02de49aea54da239")

	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
