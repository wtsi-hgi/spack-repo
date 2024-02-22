# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNotebookutils(RPackage):
	"""Dummy R APIs Used in 'Azure Synapse Analytics' for Local
Developments

	This is a pure dummy interfaces package which mirrors 'MsSparkUtils' APIs <https://learn.microsoft.com/en-us/azure/synapse-analytics/spark/microsoft-spark-utilities?pivots=programming-language-r> of 'Azure Synapse Analytics' <https://learn.microsoft.com/en-us/azure/synapse-analytics/> for R users,
    customer of Azure Synapse can download this package from CRAN for local development.
	"""
	
	cran = "notebookutils" 

	version("1.5.1", md5="56fd158c762cb2cbc75af02f87101a29")

