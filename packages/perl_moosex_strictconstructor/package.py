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
#     spack install perl-moosex-strictconstructor
#
# You can edit this file again by typing:
#
#     spack edit perl-moosex-strictconstructor
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlMoosexStrictconstructor(PerlPackage):
    """Make your object constructors blow up on unknown attributes."""

    homepage = "https://metacpan.org/pod/MooseX::StrictConstructor"
    url = "https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/MooseX-StrictConstructor-0.21.tar.gz"

    version("0.21", sha256="c72a5ae9583706ccdec71d401dcb3054013a7536b750df1436613d858ea2920d")
    version("0.20", sha256="01d451e89fd539499d742419685feafe3d12b47dcbfc8a430634942b5e50c9aa")
    version("0.19", sha256="486573c16901e83c081da3d90a544281af1baa40bbf036337d6fa91994e48a31")
    version("0.18", sha256="af6436908c126b0f4bdf859a42bcb4416cdf9cf5bb332b7d30ba752f72d8c90f")
    version("0.17", sha256="cea7a1b670aaff91f1908f7c9d28c9531da69cfec9a7b8886d3a58ce573b0a38")
    version("0.16", sha256="01c5f364f5d0fa030eeaf0dad99d9d58d9db3f6010784a733d8e54ce1b0d51f3")
    version("0.15", sha256="8edca696a3912f67b3902fad0c09e4a12e89054ded150e30b96b3ced86d755b9")
    version("0.14", sha256="9114036a96d2f3981457101da27b5e2d2e528ae202b3cc86aa4a5cd77554cc89")
    version("0.13", sha256="cb4842a16475ff73a9d137c77ba57a703f33477503291becfe49edbbd914a0fe")
    version("0.12", sha256="5a0dbac64e904b877a0497c1c8860d44d415eb426543e95aa55931b965bdf50c")
    version("0.11", sha256="dd25ed66fce6d429355705cfb3f1468b9af2c45f2a7d92a949a560c81191d557")
    version("0.10", sha256="13838efc6e68152ce67f7ecf40ca18f15f7a9f5cd6a6c6abc71bf2f368a53f69")
    version("0.09", sha256="5373addfb8a9f79789c62539ccfaefd1dacfd855781f6aa692d47119a01ca22a")
    version("0.08", sha256="3c75f30f2a41497ca0dc59b28b746bf67655606dac1e8171172a6b1735b7f07d")
    version("0.07", sha256="830d02266bc03a338b6ea551da7acf2f63c2cff7680157db7fed10c72e25bf5b")
    version("0.06_02", sha256="03d064926235238e02d53102fcb295a9baec26835c51914ba06c3b5903d30e91")
    version("0.06_01", sha256="f94c5f13f67b9e7407c37e8f49391076cd20e8b8dd738d15f965b1effc1e1f77")
    version("0.06", sha256="b11d5653e7dc01cb8a7272e534a7af6daac3c914636730aabdb785ef62cd7e4a")
    version("0.05", sha256="7f3ba16414549315e1b624ff2feb843f33033e7ee005146f154e979b0afe219b")
    version("0.04", sha256="704d7cc5ca977c305b8427104e41e35e89240792511104b86c553d90280d5966")
    version("0.03", sha256="023e98535936aab47c88c3cd375ad8be5d1ecafcd33442bfbc5790d44d080ace")
    version("0.02", sha256="6669f956b90414b8463756ceeee19351a600e5d37d1713522d5722ee27e3cf83")
    version("0.01", sha256="c5d0c4bea7428f4434c558f73cd56a10645ebd1b1f19195985eb58172ad86fdd")

    depends_on("perl-moose", type=("build", "run"))
    depends_on("perl-namespace-autoclean", type=("build", "run"))
