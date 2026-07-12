# Algorithm Boundary Policy

External algorithm results must be validated before they affect user-visible or persisted state.

## Validation Boundary

Validate every external algorithm result before it:

- modifies the MRML scene;
- is persisted;
- is displayed as successful;
- is included in a report;
- is passed to another processing component.

This is defensive validation. It does not assume external developers or components are malicious. It protects the sandbox from malformed inputs, integration mistakes, version mismatches, and unsafe assumptions.

Validation should check required fields, data types, units, coordinate systems, value ranges, and explicit mock/demo labeling where applicable.
