# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVorteksexport(RPackage):
	"""Export Dataframes to 'Vorteks' Software

	Export dataframes and automatically start importing into 
    'Vorteks'. 'Vorteks Visualization Environment (VVE)' and 'Vorteks Data Manager (VDM)' will start an import. 'Vorteks Processing Environment (VPE)' will start a new project and
    add a file reader with the dataframe file already set.
    Warning: WINDOWS ONLY. Requires installation of 'Vorteks' software.
	"""
	
	cran = "VorteksExport" 

	version("0.1.8", md5="b27800f165e48ea4a9722b9275eacaf6")

