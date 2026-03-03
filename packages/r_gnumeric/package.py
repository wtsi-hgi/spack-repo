# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGnumeric(RPackage):
	"""Read Data from Files Readable by 'gnumeric'

	Read data files readable by 'gnumeric' into 'R'. Can read
        whole sheet or a range, from several file formats, including
        the native format of 'gnumeric'. Reading is done by using
        'ssconvert' (a file converter utility included in the 'gnumeric'
        distribution <http://www.gnumeric.org>) to convert
        the requested part to CSV. From 'gnumeric' files (but not other
        formats) can list sheet names and sheet sizes or read all
        sheets.
	"""
	
	cran = "gnumeric" 

	version("0.7-10", md5="83412acd4f8c6499a2fc91ac793ba6e7")

	depends_on("r@2.8.1:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
