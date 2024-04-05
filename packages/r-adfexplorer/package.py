# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdfexplorer(RPackage):
	"""Import from and Export to Amiga Disk Files

	Amiga Disk Files (ADF) are virtual
    representations of 3.5 inch floppy disks for the
    Commodore Amiga. Most disk drives from other systems
    (including modern drives) are not able to read these
    disks. To be able to emulate this system, the ADF
    format was created. This package enables you to read
    ADF files and import and export files from and to such
    virtual DOS-formatted disks.
	"""
	
	homepage = "https://github.com/pepijn-devries/adfExplorer"
	cran = "adfExplorer" 

	version("0.1.8", md5="3944247d7b04fd7babaeeef318bc2e34")
	version("0.1.6", md5="5fe06b94c3bee885f48ec1febf201f11")

	depends_on("r@2.10:", type=("build", "run"))
