# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RRmsfact(RPackage):
    """Amazing Random Facts About the World's Greatest Hacker
    
    Display a randomly selected quote about Richard M. Stallman based on the collection in the 'GNU Octave' function 'fact()' which was aggregated by Jordi Gutiérrez Hermoso based on the (now defunct) site stallmanfacts.com (which is accessible only via <http://archive.org>).
    """

    cran = "rmsfact"

    version("0.0.3", sha256="a54d20c4e7b36b9d731deeddfb160d69c34e82f1091238541439dfa45d1e4217")

