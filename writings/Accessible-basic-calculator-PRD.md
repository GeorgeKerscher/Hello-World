# Product Requirements Document: Accessible Basic Calculator

**Status:** Draft
**Last updated:** 2026-09-26
**Target:** Responsive web application
**Accessibility target:** WCAG 2.2 Level AA

## 1. Product Summary

Build a basic web calculator that supports keyboard and labeled on-screen input, standard arithmetic order of operations, ten persistent memory registers named A through J, and a retrievable calculation history. The interface must be operable and understandable with screen readers and other assistive technologies.

WCAG 2.2 AA is the conformance target, not a claim that can be established by automated checks alone. Release requires manual keyboard and assistive-technology testing in addition to automated checks.

## 2. Problem Statement

People need a simple calculator that does not depend on visual layout or pointer input. They also need named values that remain available in later browser sessions, and a way to review previous results without losing their place or receiving confusing screen-reader announcements.

## 3. Goals

- Perform accurate basic arithmetic using conventional operator precedence.
- Support keyboard entry as well as clearly named, operable buttons.
- Make all calculator functions discoverable and usable with screen readers.
- Provide ten persistent, individually addressable memory locations, A through J.
- Require confirmation before an existing memory value is replaced or deleted.
- Keep at least ten previous calculations available for review and reuse.
- Meet WCAG 2.2 AA after evaluation with automated tools and manual testing.

## 4. Non-Goals

- Scientific, graphing, financial, or unit-conversion functions.
- User accounts, cloud synchronization, or sharing data between devices.
- A claim of universal compatibility with every browser, screen reader, or assistive technology.
- Replacing professional accessibility evaluation with automated scans.

## 5. Target Users

### 5.1 Screen-reader users

Users who navigate by landmarks, headings, form controls, buttons, and live announcements, including users of NVDA, JAWS, and VoiceOver.

### 5.2 Keyboard-only users

Users who operate the complete calculator without a mouse, including users who rely on visible focus indicators.

### 5.3 Low-vision and mobile users

Users who need readable contrast, magnification or reflow, and sufficiently large touch targets.

## 6. User Stories

- As a keyboard user, I can enter an expression with digits and standard arithmetic symbols and calculate its result.
- As a screen-reader user, I can identify each control by a meaningful accessible name and hear the result or an error when it matters.
- As a user, I can save a value in any register from A through J and recall it in a later calculation.
- As a user, I am asked before replacing or deleting an existing memory value.
- As a user, I can navigate, review, and reuse at least the ten most recent calculations.
- As a mobile user, I can use the calculator at narrow viewport widths and with touch input.

## 7. Functional Requirements

### 7.1 Arithmetic and expression entry

- **FR-1:** Support addition, subtraction, multiplication, and division.
- **FR-2:** Accept standard keyboard operators `+`, `-`, `*`, and `/`; display multiplication and division with clear, familiar symbols where appropriate.
- **FR-3:** Support decimal numbers, parentheses, and unary positive and negative signs.
- **FR-4:** Evaluate parentheses first, then unary signs, then multiplication and division, then addition and subtraction. Operators at the same precedence level are evaluated left to right.
- **FR-5:** Provide a clearly labeled calculate/equal action. `Enter` and `=` calculate when focus is in the expression input; `Escape` clears the current expression. `Backspace` edits the expression when the expression input has focus.
- **FR-6:** Do not intercept ordinary typing or browser and screen-reader commands outside the calculator's input context.
- **FR-7:** Reject malformed expressions and division by zero without crashing or silently returning an incorrect value.
- **FR-8:** Present a useful error message, retain the user's expression when practical, and allow correction without requiring a pointer.
- **FR-9:** Show the current expression and result as selectable text, not solely as a canvas, image, or inaccessible custom drawing.
- **FR-10:** Define and apply a consistent numeric precision and rounding policy. Do not imply greater precision than the calculation provides.

### 7.2 On-screen controls

- **FR-11:** Provide labeled, keyboard-operable buttons for digits, decimal point, arithmetic operators, parentheses, clear, delete-last-character, and calculate.
- **FR-12:** Give each control a meaningful accessible name. Names must not depend on visual position, color, or an unlabeled symbol alone. For example, name the `*` action “Multiply” and `/` action “Divide.”
- **FR-13:** Use native buttons and form controls where practical, with visible keyboard focus and a logical focus order.
- **FR-14:** Keep focus stable during calculation. Do not move focus unexpectedly when a result or status message is updated.

### 7.3 Memory registers A through J

- **FR-15:** Provide exactly ten memory registers identified by the single letters A, B, C, D, E, F, G, H, I, and J.
- **FR-16:** Expose each register through a labeled, keyboard-operable control. Its accessible name must include the letter and its state or value, such as “Memory A, empty” or “Memory A, 42.”
- **FR-17:** Provide actions to save the current result to a selected register, recall a stored value into the expression, and delete a stored value.
- **FR-18:** Make registers easy to locate by their first letter. In the register chooser, keyboard typing of A through J must select the matching register using native first-character selection or equivalent behavior. Do not globally capture these letters or interfere with screen-reader navigation.
- **FR-19:** Saving to an empty register may complete directly. Replacing a non-empty register requires an explicit confirmation before changing its value.
- **FR-20:** Deleting a non-empty register requires an explicit confirmation. Canceling either confirmation leaves the stored value unchanged.
- **FR-21:** Confirmation dialogs must have an accessible name and description, move focus into the dialog, keep keyboard focus within it while open, support a clear cancel action, and return focus to the initiating control when closed.
- **FR-22:** Store register values across browser sessions on the same browser and device. Clearly communicate that clearing site data or using another browser/device can remove or make these values unavailable.

### 7.4 Calculation history

- **FR-23:** Keep at least the ten most recent successful calculations in a history list, including the expression and result.
- **FR-24:** Make history entries available to keyboard and screen-reader users with a useful accessible name or structure that distinguishes expression from result.
- **FR-25:** Allow a user to review a history item and reuse its result or restore its expression without unexpected navigation or focus loss.
- **FR-26:** Keep history in newest-first order and indicate when an entry is selected or restored.
- **FR-27:** Persist at least the ten most recent calculations across browser sessions on the same browser and device, using the same data-retention expectation as memory registers.

## 8. Accessibility Requirements

### 8.1 Structure and navigation

- Use semantic page regions and a descriptive page title.
- Use headings to organize the page and sections, including Calculator, Memory, and Calculation history. Heading levels must be hierarchical and usable for navigation.
- Associate visible labels and instructions with the expression input and other form controls.
- Use lists or other suitable semantic structures for repeated history and register entries.
- Ensure DOM order follows the visual and task order.

### 8.2 Keyboard and focus

- All functionality must be available from a keyboard without requiring specific timing.
- There must be no keyboard trap.
- Focus must be visible, sufficiently contrasted, and not obscured by sticky or overlapping content.
- Keyboard shortcuts must be documented accessibly in the control's accessible description when needed and must not override browser or assistive-technology commands.
- Do not assign global A-J shortcuts. A-J first-character selection applies only while the register chooser is focused.

### 8.3 Screen-reader announcements

- Expose the expression input, buttons, register chooser, register values, history, and dialogs with correct names, roles, values, and relationships.
- Announce a completed result and calculation errors through a polite status mechanism, such as a properly implemented `role="status"` or `aria-live="polite"` region.
- Announce meaningful memory actions, including a completed save, recall, or deletion, and the register letter involved.
- Do not announce every keystroke redundantly. The expression itself remains available through the labeled input; announce state changes that users otherwise might miss.
- Use assertive announcements only for time-critical or blocking errors. Do not repeatedly announce unchanged status.
- Ensure confirmation dialogs and their available actions are announced when opened.

### 8.4 Visual presentation and responsive behavior

- Meet WCAG contrast requirements for text, meaningful graphical objects, control boundaries, and focus indicators.
- Do not use color as the only way to communicate result state, errors, selected history, or memory status.
- Support text resize and reflow at narrow viewport widths and high zoom without loss of content or functionality, except where WCAG permits otherwise.
- Provide touch targets that meet WCAG 2.2 AA target-size requirements; aim for 44 by 44 CSS pixels for frequently used calculator controls where layout permits.
- Respect user text-spacing overrides and avoid clipping labels, expressions, results, and validation messages.

## 9. Persistence, Privacy, and Errors

- Persist memory registers and calculation history locally in the browser so they are available in later sessions on that same browser and device.
- Do not send expressions, results, or memory values to a server for this product's core functionality.
- Handle unavailable, blocked, or corrupted browser storage gracefully. Explain that persistence is unavailable and keep calculation usable for the current session where possible.
- Do not silently discard data when storage is full or cannot be read. Inform the user and offer a recoverable path where possible.
- The product must explain that private browsing, clearing site data, browser changes, or device changes may prevent later retrieval.

## 10. Acceptance Criteria

### 10.1 Calculation

- Given `2 + 3 * 4`, calculating returns `14`.
- Given `(2 + 3) * 4`, calculating returns `20`.
- Given `8 / 4 / 2`, calculating returns `1`, confirming left-to-right evaluation for equal-precedence operators.
- Given an invalid expression or division by zero, the user receives an understandable error, focus is not unexpectedly moved, and the error is available to a screen reader.
- A keyboard-only user can enter, edit, clear, and calculate an expression without operating a pointer.

### 10.2 Memory

- All ten registers A-J can be reached and identified by keyboard and screen reader.
- With the register chooser focused, typing a register's first letter selects that register; typing A-J elsewhere is not intercepted.
- A saved value remains available after closing and reopening the browser in the same browser profile.
- Attempting to replace or delete a populated register presents a confirmation. Cancel leaves the value intact; confirm performs the requested action.
- Confirmation dialogs are operable by keyboard and return focus to their invoking control when dismissed.

### 10.3 History

- After at least ten successful calculations, the ten most recent entries can be navigated and read without pointer input.
- Each entry exposes its expression and result distinctly.
- A history item can be reused, and the action does not unexpectedly discard the current calculation.
- At least ten entries remain available after a browser restart in the same browser profile.

### 10.4 Accessibility and compatibility

- Every visible interactive control has an accessible name, correct role, keyboard operation, and visible focus.
- Result, error, memory, and dialog state changes are announced without announcing every character typed.
- At 200% zoom and narrow mobile viewport widths, no required calculator feature is lost to clipping or horizontal scrolling, except where WCAG 2.2 allows it.
- Automated accessibility checks report no known violations in the supported test configuration; manual testing verifies applicable WCAG 2.2 AA criteria.

## 11. WCAG 2.2 AA Mapping

The following criteria are especially relevant; this list is a test-planning aid, not a substitute for evaluating every applicable success criterion.

- **1.1.1 Non-text Content:** meaningful controls and graphics have text alternatives or accessible names.
- **1.3.1 Info and Relationships:** headings, labels, lists, and control relationships are programmatically determinable.
- **1.3.2 Meaningful Sequence:** reading and focus order preserve the intended task sequence.
- **1.4.3 Contrast (Minimum):** text meets minimum contrast.
- **1.4.10 Reflow:** content works at narrow widths and high zoom without unnecessary two-dimensional scrolling.
- **1.4.11 Non-text Contrast:** controls, focus indicators, and meaningful graphical objects have sufficient contrast.
- **1.4.12 Text Spacing:** user-adjusted text spacing does not hide or break content.
- **2.1.1 Keyboard:** all functionality is keyboard-operable.
- **2.1.2 No Keyboard Trap:** focus can move into and out of each component.
- **2.4.3 Focus Order:** focus order preserves meaning and operability.
- **2.4.6 Headings and Labels:** headings and labels describe their topic or purpose.
- **2.4.7 Focus Visible:** keyboard focus is visible.
- **2.4.11 Focus Not Obscured (Minimum):** focused components are not entirely hidden by author-created content.
- **2.5.8 Target Size (Minimum):** pointer targets meet the minimum size or an applicable exception.
- **3.2.1 On Focus:** focus alone does not unexpectedly change context.
- **3.3.1 Error Identification:** input errors are identified and described in text.
- **3.3.2 Labels or Instructions:** controls have labels or instructions when needed.
- **4.1.2 Name, Role, Value:** controls expose accurate accessible properties and state.
- **4.1.3 Status Messages:** result, error, and action updates are programmatically available without requiring focus.

## 12. Verification Plan

- Run automated accessibility checks on the primary calculator view, populated memory state, history state, and confirmation dialog.
- Complete every core flow using only the keyboard.
- Test with current supported combinations of NVDA and Firefox or Chrome, JAWS and Chrome, and VoiceOver with Safari on macOS or iOS, as applicable to the release platform.
- Verify names, roles, values, focus behavior, dialog behavior, error identification, and live announcements manually.
- Test zoom, reflow, contrast, target size, text spacing, and browser storage failure.
- Include regression tests for arithmetic precedence, parentheses, unary signs, malformed expressions, and division by zero.

## 13. Open Product Decisions

- Which browsers and assistive-technology versions are in the initial support matrix?
- Should the user be able to clear all calculation history, and should that action require confirmation?
- Should decimal precision be fixed, configurable, or display-only with full internal precision?
- Should the application offer export or import of memory and history? This is outside the initial scope.
