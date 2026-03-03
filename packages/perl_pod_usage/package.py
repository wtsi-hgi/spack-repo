# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install perl-pod-usage
#
# You can edit this file again by typing:
#
#     spack edit perl-pod-usage
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlPodUsage(PerlPackage):
    """extracts POD documentation and shows usage information."""

    homepage = "https://metacpan.org/pod/Pod::Usage"
    url = "https://cpan.metacpan.org/authors/id/M/MA/MAREKR/Pod-Usage-2.03.tar.gz"

    version("2.03", sha256="7d8fdc7dce60087b6cf9e493b8d6ae84a5ab4c0608a806a6d395cc6557460744")
    version("2.0", sha256="530943a9ac3ba00404d7be8ee8572f30f6db9de123cd725af3647333a87d4fea")
    version("1.70", sha256="54fc12b61c7661e12e102e56d68f18dfbe8899482bb8f9925db2a18b8b64d43a")
    version("1.69", sha256="1a920c067b3c905b72291a76efcdf1935ba5423ab0187b9a5a63cfc930965132")
    version("1.68", sha256="20aa70e3bc9cb49cd5fb2273f34b0ea10f687efd96e8e39ed434da90a1484833")
    version("1.67", sha256="c8be6d29b0dfe304c4ddfcc140f93d4c4de7a8362ea6e2651611c288b53cc68a")
    version("1.66", sha256="b8b6221cd86cce6d008eb6c817b18cf7643ec027ee7c6f28171fdec1ab7d7c8d")
    version("1.65", sha256="31a40c63636619bd06dfaf2ace820f555a2f85c9834f87fd47fe50e148f4cda7")
    version("1.64", sha256="9cfd105173d8c570e8bc7cb4ba9a8b8c3c3118d3019fa60739e61df2623b05e5")
    version("1.63", sha256="62d8bc7d4ce80799f3d3aaf1a636bec7bed75585ddef50fd197990ba6c4bb62c")
    version("1.62", sha256="6773f9fead6478233d80602083d517bd252d251b4aba21add7b20a3fd4e2a0ce")
    version("1.61", sha256="3e0c0945f3adbf37c3170d714d88cc382bbcd926ebb663398d55b832fdb6f7f4")
    version("1.60", sha256="b94cdcb951b41376166e83f329ee366d88aec29b67509a75d4b6db2f0a7c11e7")
