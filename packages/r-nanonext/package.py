# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNanonext(RPackage):
	"""NNG (Nanomsg Next Gen) Lightweight Messaging Library

	R binding for NNG (Nanomsg Next Gen), a successor to ZeroMQ. NNG is
    a socket library implementing 'Scalability Protocols', a reliable,
    high-performance standard for common communications patterns including
    publish/subscribe, request/reply and service discovery, over in-process,
    IPC, TCP, WebSocket and secure TLS transports. As its own threaded
    concurrency framework, provides a toolkit for asynchronous programming and
    distributed computing, with intuitive 'aio' objects which resolve
    automatically upon completion of asynchronous operations, and
    synchronisation primitives allowing R to wait upon events signalled by
    concurrent threads.
	"""
	
	homepage = "https://shikokuchuo.net/nanonext/"
	cran = "nanonext" 

	version("0.13.2", md5="acfdcfda771ca9bffeff4d62baa44b32")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("cmake", type=("build", "link", "run"))
