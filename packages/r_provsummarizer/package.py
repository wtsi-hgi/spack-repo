# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProvsummarizer(RPackage):
	"""Summarizes Provenance Related to Inputs and Outputs of a Script
or Console Commands

	Reads the provenance collected by the 'rdtLite' or 'rdt' packages,
    or other tools providing compatible PROV JSON output, created by the
    execution of a script or a console session, and provides a human-readable
    summary identifying the input and output files, the scripts used (if any),
    errors and warnings produced, and the environment in which it was executed.
    It can also optionally package all the files into a zip file.  The exact
    format of the PROV JSON file created by 'rdtLite' and 'rdt' is described
    in <https://github.com/End-to-end-provenance/ExtendedProvJson>.  More
    information about 'rdtLite' and associated tools is available at
    <https://github.com/End-to-end-provenance/> and Lerner, Boose, and Perez
    (2018), Using Introspection to Collect Provenance in R, Informatics,
    <doi: 10.3390/informatics5010012>.
	"""
	
	homepage = "https://github.com/End-to-end-provenance"
	cran = "provSummarizeR" 

	version("1.5.1", md5="9847833b38cd69d67942cdf6d3c592d9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-provparser@1:", type=("build", "run"))
