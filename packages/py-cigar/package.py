# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCigar(PythonPackage):
    """cigar is a simple library for dealing with cigar strings. the most useful
feature now is soft-masking from left or right. This allows one to adjust
a SAM record only by changing the cigar string to soft-mask a number of bases
such that the rest of the SAM record (pos, tlen, etc.) remain valid, but
downstream tools will not consider the soft-masked bases in further analysis."""

    homepage = "https://github.com/brentp/cigar"
    pypi = "cigar/cigar-0.1.3.tar.gz"

    version("0.1.3", sha256="5847f5e8968035b3a5b04dcfa879fb6c14dd3a42dce8994864806dcda8a4fcf2")
