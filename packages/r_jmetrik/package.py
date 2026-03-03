# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmetrik(RPackage):
	"""Tools for Interacting with 'jMetrik'

	The main purpose of this package is to make it easy for userR's to interact with 'jMetrik' an open source application for psychometric analysis. For example it allows useR's to write data frames to file in a format that can be used by 'jMetrik'. It also allows useR's to read *.jmetrik files (e.g. output from an analysis) for follow-up analysis in R. The *.jmetrik format is a flat file that includes a multiline header and the data as comma separated values. The header includes metadata about the file and one row per variable with the following information in each row: variable name, data type, item scoring, special data codes, and variable label. 
	"""
	
	cran = "jmetrik" 

	version("1.1", md5="0a9f30bd517c896cfad08f1ed5193a47")

