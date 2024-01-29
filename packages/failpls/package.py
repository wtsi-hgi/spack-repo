# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Failpls(Package):
    """Azimuth is a Shiny app demonstrating a query-reference mapping algorithm for single-cell data."""

    homepage = "https://satijalab.org/azimuth"
    git = "https://github.com/satijalab/azimuth/"

    version("0.4.6", tag="v0.4.6")

