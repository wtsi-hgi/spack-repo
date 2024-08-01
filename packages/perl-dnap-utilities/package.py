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
#     spack install perl-dnap-utilities
#
# You can edit this file again by typing:
#
#     spack edit perl-dnap-utilities
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlDnapUtilities(PerlPackage):
    """DNA Pipelines Perl Utility Library

    These modules are used by several Perl libraries written by the WTSI
    NPG team for use by WTSI DNA Pipelines."""

    homepage = "https://github.com/wtsi-npg/perl-dnap-utilities"
    url = "https://github.com/wtsi-npg/perl-dnap-utilities/archive/refs/tags/0.7.0.tar.gz"

    version("0.7.0", sha256="9d5aff873defc196e7a240df13f45bcfeea6f2b9ad959b490adb3de4961e1610")
    version("0.5.7", sha256="89bd2ab45de5032b529c774c929c0d2782aac15c89d24eb108a7c1fa9745c02b")
    version("0.5.6", sha256="36038b3ca158bcae5e3f48af0036489d07458457cf6673cafc1a4b62cc99ac3a")
    version("0.5.5", sha256="6a8a05da224daa227e2e49df7476ebcffd131cf40c5ba177bf8b73ace01b0e42")
    version("0.5.4", sha256="a3ba45642ee06cf2723f40a4a85a8fc49735fd351f8789c9be7e31274b5ff7ea")
    version("0.5.3", sha256="0f0e2865697b5098dd33d02484879aa6830d96e965366f1cf04889c4d82b3580")
    version("0.5.2", sha256="98f11caf0e4e8cf64e29eb09ac7225ebab8cb9e72cc71b81962e77975139716b")
    version("0.5.1", sha256="d9a1b961d98d76156ecca939a0e10e00dd34b7a1240d8221bd919d06433baf70")
    version("0.5.0", sha256="ca271550d8ec96af46e529c8e5380fe4bd0139842a165c36b2faaf7cbf7fe87d")
    version("0.4.2", sha256="cf041c8521486d1954ea55ea9dbbfce3ada54b2dcdb5843b4475716b98b0db8b")
    version("0.4.1", sha256="e0cff59687ea7e1475b72d5747768e812ebd74d6909ea26d56c2e9f8281ccba2")

    depends_on("perl-module-build", type="build")

    # FIXME: Add additional dependencies if required:
    # depends_on("perl-foo", type=("build", "run"))

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
