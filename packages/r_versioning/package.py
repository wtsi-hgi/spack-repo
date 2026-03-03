# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVersioning(RPackage):
	"""Settings and File I/O using a Configuration YAML File

	R data pipelines commonly require reading and writing data to versioned 
    directories. Each directory might correspond to one step of a multi-step process,
    where that version corresponds to particular settings for that step and a chain of
    previous steps that each have their own versions. This package creates a configuration
    object that makes it easy to read and write versioned data, based on YAML
    configuration files loaded and saved to each versioned folder.
	"""
	
	cran = "versioning" 

	version("0.1.0", md5="3c13193201c9bc1c92f0867645e5b3eb")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
