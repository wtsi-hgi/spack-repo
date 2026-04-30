# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyGffutils(PythonPackage):
    """GFF and GTF file manipulation and interconversion

    gffutils is a Python package for working with and manipulating the GFF and
    GTF format files typically used for genomic annotations. Files are loaded
    into a sqlite3 database, allowing much more complex manipulation of
    hierarchical features (e.g., genes, transcripts, and exons) than is
    possible with plain-text methods alone."""

    homepage = "https://github.com/daler/gffutils"
    pypi = "gffutils/gffutils-0.10.1.tar.gz"

    maintainers("dorton21")

    license("MIT")

    version("0.14", sha256="0246a16373453a5a1faf6696553557f2ebf49b2f91a7730cb59d46b5cbd1d9b1")
    version("0.13", sha256="b0d52f35c014cc0330fb5c4e3c6fea127c90ccf4c5384a825cdb5c8ff330d4eb")
    version("0.12", sha256="b31e261db5bd8737cb712c361c129eb2c373ef62f03b62770320589f10da1983")
    version("0.11.1", sha256="ca7bf814d600b389bb2d5c403dd279755118cb1476c19c6f7aecb8c51a84263c")
    version("0.11.0", sha256="4593bdf8bda2501b8e0c54cd3366fdaba04b211c86f43c0029e65869d15ec769")
    version("0.10", sha256="9b1f5f30d93754e8c67503b94878dbd7d113a5acf8d04c4c363aa8a78a506b2d")
    version("0.9", sha256="e1b0bf2b422ec3491be13d77bf7baf71d274abd844e8f8b6c1217a95b236218b")
    version("0.8.7.1", sha256="0fd612cdf37b9aeb0d3504bd45acde1b00574554b84095a683688595337e94e6")
    version("0.8.7", sha256="4fb2c95dbf7f98e537d00995eb7aa6bf36ee70fd9a707aa3df2202c898d54c01")
    version("0.8.6.1", sha256="e421a06ef916041946f6b1dc3ae85776524c6bc3578bdbdda5f7e98d8a3d8db4")
    version("0.8.6", sha256="6cdfb77b57ef22b5971e5d876bcc89e05a5e6194589d1e283b5e9d6df83fff46")
    version("0.8.5", sha256="c5acd59c55662fe082fa78bc5d5ae383e73040f7610ef8d45b8bd62d9fae74d8")
    version("0.8.4rc1", sha256="63d3ec216bb395ff8d9f9033f8aa83f82130e4ef229273e37beb1034580da666")
    version("0.8.3.1", sha256="6939ff831bb2e6a33a2c99d4c57ce64b1c517ca56be3014b4171d45a86964508")
    version("0.8.3", sha256="9f28733ed6f9603817691c0ac14078792f7f853054ee90bc401320a495d218f2")
    version("0.8.2", sha256="fc85976687bb8ff6742daebd7e3d3fcbf47bfda4ab8ef7e02c8b155b733ba8ac")
    version("0.8.1", sha256="1994525e35cbf32d1a5679e9bf708b84778fb760d7889c917dd7cb571bb06ff4")
    version("0.8", sha256="5eda5e365352b3c7f84fe6cff4b4f69a2c8d7ba6ea5403d53e1bb7718cd3c13f")
    version("0.7", sha256="1e03365ed45a1dafb8ff750a562930872dc09cdd86603e3f34c81a4183571546")
    version("0.10.1", sha256="a8fc39006d7aa353147238160640e2210b168f7849cb99896be3fc9441e351cb")

    depends_on("py-setuptools", type="build")
    depends_on("py-pyfaidx@0.5.5.2:", type=("build", "run"))
    depends_on("py-six@1.12.0:", type=("build", "run"))
    depends_on("py-argh@0.26.2:", type=("build", "run"))
    depends_on("py-argcomplete@1.9.4:", type=("build", "run"))
    depends_on("py-simplejson", type=("build", "run"))